# Qt6 app runner (`/qtapp/`)

A small in-browser runner for Qt6-wasm packages published to the
[emscripten-forge-4x-experimental](https://prefix.dev/channels/emscripten-forge-4x-experimental)
channel. Given the URL of a `.tar.bz2` package (or a locally-picked file),
it fetches, unpacks, and boots the Qt app entirely client-side.

**Try it**: <https://emscripten-forge.org/qtapp/>

## Available apps

Currently on the
[emscripten-forge-4x-experimental](https://prefix.dev/channels/emscripten-forge-4x-experimental)
channel:

- **[qt-calculator](https://emscripten-forge.org/qtapp/?pkg=https%3A%2F%2Frepo.prefix.dev%2Femscripten-forge-4x-experimental%2Femscripten-wasm32%2Fqt-calculator-experimental-6.11.2-hc780342_0.tar.bz2)** —
  Qt's own upstream calculator example
  ([recipe](https://github.com/emscripten-forge/recipes/tree/main/recipes/recipes_emscripten/qt-calculator-experimental)).
- **[sqlitebrowser](https://emscripten-forge.org/qtapp/?pkg=https%3A%2F%2Frepo.prefix.dev%2Femscripten-forge-4x-experimental%2Femscripten-wasm32%2Fsqlitebrowser-experimental-3.13.99-h8b281d3_0.tar.bz2)** —
  DB Browser for SQLite: create tables, run queries, download `.sqlite` files
  ([recipe](https://github.com/emscripten-forge/recipes/tree/main/recipes/recipes_emscripten/sqlitebrowser-experimental)).

The exact `.tar.bz2` filename changes on each rebuild (build hash suffix);
browse the [channel index](https://prefix.dev/channels/emscripten-forge-4x-experimental)
for current URLs.

## Deep-links

Append `?pkg=<URL-encoded package URL>` to auto-load a package on page
open. Both parameters (`?pkg=` and `?fullscreen=1`) can be shared as
regular URLs. Combine as `?pkg=…&fullscreen=1` to start with the top
and status bars hidden.

## How it works

1. Fetches the `.tar.bz2` (or reads it via file picker / drag-and-drop).
2. Decodes bzip2 and walks the tar entries via
   [`@emscripten-forge/untarjs`](https://www.npmjs.com/package/@emscripten-forge/untarjs).
3. Locates the app under `share/<name>/` inside the package.
4. Wraps every file in that directory as a `blob:` URL, then loads Qt's
   `qtloader.js` and the app's Emscripten glue against those blobs.
5. Fires a synthetic `resize` shortly after boot to work around a
   Qt6-wasm quirk where the first paint doesn't commit until a resize.

## Package requirements

Any Qt6-wasm recipe on this channel that produces
`share/<name>/{<name>.wasm, <name>.js, qtloader.js}` is loadable. The
runner discovers the app name by scanning for the sole `share/*/*.wasm`
file, so nothing else needs to be configured. Packages must be built
against `qt6-main-jspi` (JavaScript Promise Integration is what lets
Qt's event loop yield to the browser).

## Browser requirements

Qt6-wasm on this channel uses JSPI, which needs:

- Chrome 137+ (April 2025)
- Firefox 141+ (July 2025)
- Safari 18.4+ (April 2025)

## Known limitations

- **Continuous animation at 60fps** — Qt-wasm timer-driven animation under
  JSPI can starve the browser main thread. Static and event-driven UIs
  (calculators, editors, viewers) work fine; games and animated demos
  need a different tick source.
- **Dynamic side-module deps** (e.g. openblas as a runtime `.so`) — not
  yet supported. The runner only knows about the app's own artifacts.
- **Only `.tar.bz2`** — `.conda` format (zstd-inside-zip) would need
  additional decoders.
