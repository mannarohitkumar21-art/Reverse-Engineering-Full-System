# Releases and ZIP downloads

A GitHub Actions workflow at `.github/workflows/release.yml` packages the repository and attaches a ZIP to each tag matching `v*`.

To publish the first release:

```bash
git tag v1.0.0
git push origin v1.0.0
```

The workflow creates the GitHub Release and uploads `Universal-RE-Engine-v1.0.0.zip`.

Latest release page:
`https://github.com/mannarohitkumar21-art/universal-re-engine/releases/latest`

Versioned direct asset URL:
`https://github.com/mannarohitkumar21-art/universal-re-engine/releases/download/v1.0.0/Universal-RE-Engine-v1.0.0.zip`

The direct URL works after the workflow has successfully published that release asset.
