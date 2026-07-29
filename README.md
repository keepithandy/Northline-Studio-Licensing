# Northline Studio Licensing

This repository is the public licensing and intellectual-property policy hub for works published under the **Northline Studio** name by **Johnny Belles**. It provides documentation and intake processes, not legal advice, legal certification, or government registration.

## License model

Northline Studio projects use a split-license model:

- **Source code:** governed only by the license and notices expressly included with the applicable project or file.
- **Creative content and assets:** All Rights Reserved unless a controlling project or asset notice grants different terms.
- **Third-party material:** governed by its original license and attribution requirements.

Creative content includes artwork, logos, icons, audio, music, sound effects, writing, lore, worldbuilding, characters, item names, screenshots, store-page material, and other game or brand assets.

## Authority and conflicts

The license or notice included in an individual project, file, or third-party component controls when it conflicts with this summary. The [project catalog](PROJECTS.md) is an index rather than a license grant. See [fictional precedence examples](docs/CONFLICT_PRECEDENCE.md) for common cases.

## Maintenance resources

- [Split-license onboarding checklist](docs/ONBOARDING_CHECKLIST.md)
- [Project catalog](PROJECTS.md)
- [Creative-content terms](ASSETS_LICENSE.md)
- [Third-party attribution template](docs/THIRD_PARTY_ATTRIBUTION_TEMPLATE.md)
- [Creative-asset provenance template](docs/ASSET_PROVENANCE_TEMPLATE.md)
- [Per-project audit checklist](docs/PROJECT_AUDIT_CHECKLIST.md)
- [Plain-language FAQ](docs/FAQ.md)
- [Policy change log](CHANGELOG.md)

## Permission requests

Use the repository's **Licensing or permission request** issue form for commercial use, redistribution, adaptation, asset use, or another permission not expressly granted. Do not publish confidential material in a public issue; state that private follow-up is required. Submission does not grant permission, promise approval, establish exclusivity, or guarantee a response time.

## Validation

Run the non-mutating local-link check with:

```powershell
python tools/check_links.py
```

GitHub Actions runs the same check on pull requests and `main`. External links remain human-reviewed because temporary network failures must not be confused with missing repository files.