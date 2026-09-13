(function () {
  "use strict";

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

  var chrome = document.createElement("div");
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
