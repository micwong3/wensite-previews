/* ==========================================================================
 * Wensite preview visit/click logging (fail-silent).
 * Posts one JSON event per page_view / cta_click / activate_click to a
 * Google Apps Script web app that appends a row to "Wensite Preview Visits".
 * Source for the sink: _ops/preview-visit-logger.gs  (see _ops/PREVIEW_VISIT_LOGGING.md)
 * ========================================================================== */
var TRACK_ENDPOINT = ""; // <- paste Apps Script web app /exec URL here ("" = logging disabled)

(function () {
  "use strict";
  try {
    var W = window, D = document, B = D.body;
    var PV_DEDUPE_MS = 30 * 60 * 1000;
    var BOT_RE = /bot|crawl|spider|slurp|preview|facebookexternalhit|WhatsApp|Slackbot|TelegramBot|Twitterbot|LinkedInBot|Discordbot|Googlebot|bingbot|Applebot|HeadlessChrome|curl|wget|python-requests|Go-http-client/i;

    var params;
    try { params = new URLSearchParams(W.location.search); } catch (e) { params = { get: function () { return null; } }; }

    function ssGet(k) { try { return W.sessionStorage.getItem(k); } catch (e) { return null; } }
    function ssSet(k, v) { try { W.sessionStorage.setItem(k, v); } catch (e) {} }
    function lsGet(k) { try { return W.localStorage.getItem(k); } catch (e) { return null; } }
    function lsSet(k, v) { try { W.localStorage.setItem(k, v); } catch (e) {} }
    function lsDel(k) { try { W.localStorage.removeItem(k); } catch (e) {} }
    function trunc(s, n) { s = s == null ? "" : String(s); return s.length > n ? s.slice(0, n) : s; }

    // Slug: body[data-preview-slug]; activate.html falls back to ?biz=
    var slug = (B && B.getAttribute("data-preview-slug")) || params.get("biz") || "";

    // src: ?s= on landing, persisted per slug for the visit (sessionStorage)
    var srcKey = "wensite_src_" + slug;
    var srcParam = params.get("s");
    if (srcParam) ssSet(srcKey, trunc(srcParam, 40));
    var src = trunc(srcParam || ssGet(srcKey) || "", 40);

    // is_test: ?test=1 (sticky in localStorage), ?test=0 clears; localhost always test
    var testKey = "wensite_is_test";
    var testParam = params.get("test");
    if (testParam === "1") lsSet(testKey, "1");
    else if (testParam === "0") lsDel(testKey);
    var host = (W.location.hostname || "").toLowerCase();
    var is_test = lsGet(testKey) === "1" || host === "localhost" || host === "127.0.0.1" || W.location.protocol === "file:";

    var uaFull = (W.navigator && W.navigator.userAgent) || "";
    var is_bot = BOT_RE.test(uaFull) || !!(W.navigator && W.navigator.webdriver);

    function pageFromPath(path) {
      var p = (path || "").toLowerCase();
      if (/activate(\.html)?\/?$/.test(p) || /\/activate\//.test(p)) return "activate";
      if (/\/services(\/|\.html|$)/.test(p)) return "services";
      if (/\/contact(\/|\.html|$)/.test(p)) return "contact";
      if (/(^|\/)(index\.html)?$/.test(p)) return "home";
      return "other";
    }

    function tsET(d) {
      try {
        var parts = {};
        new Intl.DateTimeFormat("en-US", {
          timeZone: "America/New_York", hourCycle: "h23",
          year: "numeric", month: "2-digit", day: "2-digit",
          hour: "2-digit", minute: "2-digit", second: "2-digit"
        }).formatToParts(d).forEach(function (x) { parts[x.type] = x.value; });
        var hh = parts.hour === "24" ? "00" : parts.hour;
        var asUTC = Date.UTC(+parts.year, +parts.month - 1, +parts.day, +hh, +parts.minute, +parts.second);
        var off = Math.round((asUTC - Math.floor(d.getTime() / 1000) * 1000) / 60000);
        var sign = off < 0 ? "-" : "+", a = Math.abs(off);
        var oh = Math.floor(a / 60), om = a % 60;
        return parts.year + "-" + parts.month + "-" + parts.day + "T" + hh + ":" + parts.minute + ":" + parts.second +
          sign + (oh < 10 ? "0" : "") + oh + ":" + (om < 10 ? "0" : "") + om;
      } catch (e) { return d.toISOString(); }
    }

    function send(eventName) {
      try {
        if (!TRACK_ENDPOINT) return;
        var path = W.location.pathname || "/";
        var payload = JSON.stringify({
          ts_et: tsET(new Date()),
          preview_slug: slug,
          event: eventName,
          page: pageFromPath(path),
          path: trunc(path, 300),
          referrer: trunc(D.referrer || "", 300),
          ua: trunc(uaFull, 180),
          src: src,
          is_test: is_test,
          is_bot: is_bot
        });
        // text/plain => CORS "simple request": no preflight (Apps Script can't answer OPTIONS)
        var sent = false;
        if (W.navigator && typeof W.navigator.sendBeacon === "function") {
          try { sent = W.navigator.sendBeacon(TRACK_ENDPOINT, new Blob([payload], { type: "text/plain;charset=UTF-8" })); } catch (e) { sent = false; }
        }
        if (!sent && typeof W.fetch === "function") {
          W.fetch(TRACK_ENDPOINT, {
            method: "POST", mode: "no-cors", keepalive: true, credentials: "omit",
            headers: { "Content-Type": "text/plain;charset=UTF-8" }, body: payload
          }).catch(function () {});
        }
      } catch (e) {}
    }

    // 1) page_view, deduped per slug+path for 30 min in this tab session
    try {
      var pvKey = "wensite_pv_" + slug + "_" + (W.location.pathname || "/");
      var last = parseInt(ssGet(pvKey) || "", 10);
      var now = Date.now();
      if (!(last > 0 && now - last < PV_DEDUPE_MS)) {
        ssSet(pvKey, String(now));
        send("page_view");
      }
    } catch (e) {}

    // 2/3) clicks — delegated (capture) so dynamically injected chrome links count too.
    var ACTIVATE_SEL = '.ws-activate, [data-ws-activate], [data-ws-activate-link], a[href*="activate.html"], a[href="#activate"]';
    var CTA_SEL = ".btn-primary, .nav-cta, .home-actions .btn-primary";
    D.addEventListener("click", function (e) {
      try {
        var t = e.target;
        if (!t || !t.closest) return;
        if (t.closest(ACTIVATE_SEL)) send("activate_click");
        else if (t.closest(CTA_SEL)) send("cta_click");
      } catch (err) {}
    }, true);

    W.__wensiteTrack = { send: send, slug: slug, src: src, is_test: is_test, is_bot: is_bot };
  } catch (e) {}
})();

(function () {
  "use strict";

  // activate.html loads this file with data-ws-track-only: logging only, no chrome UI
  var me = document.currentScript;
  if (me && me.hasAttribute("data-ws-track-only")) return;

  var body = document.body;
  var slug = body.getAttribute("data-preview-slug") || "preview";
  var name = body.getAttribute("data-preview-name") || "this business";
  var hoursKey = "wensite_hours_" + slug;
  var startKey = "wensite_start_" + slug;

  function hoursForSlug() {
    var stored = parseFloat(localStorage.getItem(hoursKey) || "");
    if (stored >= 48 && stored <= 72) return stored;
    var hours = 48 + Math.random() * 24;
    localStorage.setItem(hoursKey, String(hours));
    return hours;
  }

  function startForSlug() {
    var stored = parseInt(localStorage.getItem(startKey) || "", 10);
    if (stored > 0) return stored;
    var now = Date.now();
    localStorage.setItem(startKey, String(now));
    return now;
  }

  function pad(n) {
    return n < 10 ? "0" + n : String(n);
  }

  function remainingMs() {
    var end = startForSlug() + hoursForSlug() * 3600 * 1000;
    return end - Date.now();
  }

  function format(ms) {
    if (ms <= 0) return "Expired";
    var total = Math.floor(ms / 1000);
    var h = Math.floor(total / 3600);
    var m = Math.floor((total % 3600) / 60);
    var s = total % 60;
    return pad(h) + ":" + pad(m) + ":" + pad(s);
  }

  /** Resolve path to repo-root activate.html for multi-page stamps. */
  function activateHref() {
    var custom = body.getAttribute("data-activate-href");
    if (custom) return custom;
    var root = body.getAttribute("data-ws-root");
    if (root) {
      root = root.replace(/\/?$/, "/");
      return root + "activate.html?biz=" + encodeURIComponent(slug);
    }
    // Legacy default: nested v1/ style (3 levels up from page)
    return "../../../activate.html?biz=" + encodeURIComponent(slug);
  }

  // Stamped pages ship this bar pre-rendered in the HTML (_ops/perf_inline.py) so it is painted with
  // the first frame and nothing shifts when this script runs; otherwise build it here as before.
  var chrome = document.querySelector(".ws-chrome[data-ws-prerendered]");
  if (chrome) {
    var pre = chrome.querySelector("[data-ws-activate]");
    if (pre) pre.setAttribute("href", activateHref());
  } else {
    chrome = document.createElement("div");
    chrome.className = "ws-chrome";
    chrome.setAttribute("role", "banner");
    chrome.innerHTML =
      '<div class="ws-chrome-inner">' +
        '<div class="ws-chrome-copyblock">' +
          '<div class="ws-chrome-top">' +
            '<span class="ws-badge">Private preview</span>' +
            '<span class="ws-timer" data-ws-timer aria-live="polite">—</span>' +
          "</div>" +
          '<p class="ws-copy">A private rebuild for <strong>' +
            name.replace(/</g, "&lt;") +
          "</strong>. Not a live site — claim it before this preview expires.</p>" +
        "</div>" +
        '<a class="ws-activate" data-ws-activate href="' +
          activateHref() +
        '">Activate this site — $99/mo</a>' +
      "</div>";

    body.insertBefore(chrome, body.firstChild);
  }

  body.classList.add("ws-has-chrome");

  var timerEl = chrome.querySelector("[data-ws-timer]");

  function tick() {
    var ms = remainingMs();
    timerEl.textContent = ms <= 0 ? "Expired" : "Expires in " + format(ms);
    chrome.classList.toggle("ws-expired", ms <= 0);
  }

  tick();
  setInterval(tick, 1000);

  document.querySelectorAll('a[href="#activate"]').forEach(function (a) {
    a.addEventListener("click", function (e) {
      var target = document.getElementById("activate");
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: "smooth", block: "start" });
      } else {
        e.preventDefault();
        window.location.href = activateHref();
      }
    });
  });

  // Any in-page .ws-activate-link mirrors chrome Activate destination
  document.querySelectorAll("[data-ws-activate-link]").forEach(function (a) {
    a.setAttribute("href", activateHref());
  });
})();
