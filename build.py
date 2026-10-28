"""Builds docs/index.html (the phone app) from app.html, the single source for the page.

app.html is written without <html>/<head>/<body> so it can also be published as a Claude preview.
This wraps it in a full document with the phone-app tags (home screen icon, full-screen mode).
"""
from pathlib import Path

ROOT = Path(__file__).parent
app = (ROOT / "app.html").read_text()

head = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#171b21" media="(prefers-color-scheme: dark)">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Hoops">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon-192.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<style>*,*::before,*::after{box-sizing:border-box}:root{padding-top:env(safe-area-inset-top,0px)}body{margin:0}img{max-width:100%}</style>
</head>
<body>
"""
# The preview-only tag isn't needed on the real site
app = app.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")
(ROOT / "docs" / "index.html").write_text(head + app + "\n</body>\n</html>\n")
print("built docs/index.html")
