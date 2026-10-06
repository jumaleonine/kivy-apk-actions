# kivy-apk-actions

Build an Android APK from your Python/Kivy app **in the cloud**, with no Linux machine, no Android Studio, and no local setup. Push to GitHub, download the APK.

![Build](https://github.com/YOUR-USERNAME/kivy-apk-actions/actions/workflows/build-apk.yml/badge.svg)

## Why this exists

Buildozer is the standard way to package Kivy apps, but it only runs on Linux/macOS and the first setup is painful. This template moves the whole build into GitHub Actions so it works from any computer, or even a phone.

## Features

- Runs your tests first, then builds the APK
- Caches the Android SDK/NDK so later builds are much faster
- Uploads the APK as a downloadable artifact on every push
- Publishes a GitHub Release automatically when you push a version tag
- Includes a tiny working Kivy app and unit tests to start from

## Quick start

1. Click **Use this template** (or fork), then clone your copy.
2. Edit `buildozer.spec`: set `title`, `package.name`, and `package.domain`.
3. Replace `main.py` with your own app. Keep logic in separate modules so it stays testable.
4. Push to `main`.
5. Open the **Actions** tab, wait for the build, then download the `apk` artifact.

The first build takes roughly 20-40 minutes. Cached builds are much faster.

## Make a release

```bash
git tag v0.1.0
git push origin v0.1.0
```

The workflow builds the APK and attaches it to a new GitHub Release.

## Add dependencies

List them in `buildozer.spec`:

```ini
requirements = python3,kivy==2.3.0,requests,pillow
```

Every library must be supported by python-for-android. Pure-Python packages usually work; heavy native libraries often need a recipe.

## Run locally

```bash
pip install -r requirements-dev.txt
pytest
python main.py
```

## Troubleshooting

| Problem | Likely fix |
|---|---|
| App crashes on launch | A package is missing from `requirements` in `buildozer.spec` |
| `Aidl not found` or license errors | Keep `android.accept_sdk_license = True` |
| Build runs out of time | Re-run; the second run reuses the cache |
| Cython errors | Keep the `cython<3` pin in the workflow |
| Missing file in app | Add its extension to `source.include_exts` |

To see why an app crashed on a phone, connect it by USB and run `adb logcat | grep python`.

## Project layout

```
main.py                      Kivy UI
core.py                      App logic (unit-tested)
tests/                       pytest tests
buildozer.spec               Android build config
.github/workflows/           CI: test, build, release
```

## Contributing

Issues and pull requests are welcome. If a build breaks on a new Buildozer or Kivy release, please open an issue with the log.

## License

Juma Leonine
