// OPTIONAL. Only needed if ESPN stops letting the app read its feed directly.
// Deploy as a free Cloudflare Worker, then put its address in RELAY at the top of app.html's script.
// It forwards scoreboard requests to ESPN and adds the header browsers need.
export default {
  async fetch(request) {
    const url = new URL(request.url);
    if (!url.pathname.startsWith("/apis/site/v2/sports/basketball/mens-college-basketball/")) {
      return new Response("Not found", { status: 404 });
    }
    const upstream = await fetch("https://site.api.espn.com" + url.pathname + url.search, {
      cf: { cacheTtl: 15, cacheEverything: true },
    });
    const res = new Response(upstream.body, upstream);
    res.headers.set("Access-Control-Allow-Origin", "*");
    return res;
  },
};
