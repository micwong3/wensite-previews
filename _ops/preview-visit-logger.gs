/**
 * Wensite preview visit logger — Google Apps Script web app.
 * Appends one row per event to the "Wensite Preview Visits" sheet.
 *
 * Deploy: Deploy > New deployment > type "Web app"
 *   Execute as: Me (michaelwong0818@gmail.com)
 *   Who has access: Anyone
 * Then paste the /exec URL into TRACK_ENDPOINT at the top of shared/preview-chrome.js.
 *
 * CORS note: Apps Script web apps cannot answer OPTIONS preflights or set custom
 * response headers. The client therefore sends a CORS "simple request"
 * (POST, Content-Type text/plain) via sendBeacon / fetch(no-cors), which never
 * preflights. doPost still runs server-side and the row lands; Google's
 * googleusercontent.com redirect response carries Access-Control-Allow-Origin: *.
 */

var SHEET_ID = '1hj6xY9_dzfzZRC4LMsFp2IOVcxqsC4gczMd_hV2I5ro'; // Wensite Preview Visits
var COLS = ['ts_et', 'preview_slug', 'event', 'page', 'path', 'referrer', 'ua', 'src', 'is_test', 'is_bot'];
var EVENTS = { page_view: 1, cta_click: 1, activate_click: 1 };
var PAGES = { home: 1, services: 1, contact: 1, activate: 1, other: 1 };
var MAX_ROWS_PER_REQUEST = 20;

function doPost(e) {
  try {
    var raw = (e && e.postData && e.postData.contents) || '';
    var data;
    try { data = JSON.parse(raw); } catch (err) { data = (e && e.parameter) || {}; }
    var items = Array.isArray(data) ? data.slice(0, MAX_ROWS_PER_REQUEST) : [data];
    var rows = [];
    for (var i = 0; i < items.length; i++) {
      var r = toRow_(items[i]);
      if (r) rows.push(r);
    }
    if (rows.length) append_(rows);
    return json_({ ok: true, appended: rows.length });
  } catch (err) {
    return json_({ ok: false, error: String(err) });
  }
}

/** Health check: GET /exec -> {"ok":true,...}. Does not write. */
function doGet() {
  return json_({ ok: true, sink: 'wensite-preview-visits', cols: COLS });
}

function toRow_(d) {
  if (!d || typeof d !== 'object') return null;
  var ev = str_(d.event, 32);
  if (!EVENTS[ev]) return null; // drop junk
  var page = str_(d.page, 16);
  if (!PAGES[page]) page = 'other';
  var ts = str_(d.ts_et, 40) ||
    Utilities.formatDate(new Date(), 'America/New_York', "yyyy-MM-dd'T'HH:mm:ssXXX");
  return [
    safe_(ts),
    safe_(str_(d.preview_slug, 80)),
    ev,
    page,
    safe_(str_(d.path, 300)),
    safe_(str_(d.referrer, 300)),
    safe_(str_(d.ua, 180)),
    safe_(str_(d.src, 40)),
    bool_(d.is_test),
    bool_(d.is_bot)
  ];
}

function append_(rows) {
  var lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    var sh = SpreadsheetApp.openById(SHEET_ID).getSheets()[0];
    if (sh.getLastRow() === 0) sh.appendRow(COLS);
    sh.getRange(sh.getLastRow() + 1, 1, rows.length, COLS.length).setValues(rows);
  } finally {
    lock.releaseLock();
  }
}

function str_(v, n) { v = v == null ? '' : String(v); return v.length > n ? v.slice(0, n) : v; }
function bool_(v) { return v === true || v === 'true' || v === 1 || v === '1'; }
/** Block spreadsheet formula injection. */
function safe_(s) { return /^[=+\-@]/.test(s) ? "'" + s : s; }
function json_(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}
