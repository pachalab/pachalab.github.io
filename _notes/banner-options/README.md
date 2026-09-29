# Banner image study

Seven shortlisted images for Quito, Marseille, Freiburg, and Dallas. Open `preview.html` to compare 4:1, 3:1, and 16:9 crops, adjust the crop position, and show or hide a text overlay. The downloaded image files are unchanged; crops are previewed in the browser.

This folder is a local design study under `_notes/`, excluded from the Quarto build. No banner has been applied to the website.

## Selection

| Candidate | Downloaded size | Author and license | Source |
|---|---|---|---|
| [Dallas — skyline at dusk](images/dallas-skyline-dusk.jpg) | 3840 × 1211 | Matthew T Rader · [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) | [Source](https://commons.wikimedia.org/wiki/File:Dallas_Skyline_at_Dusk.jpg) |
| [Dallas — skyline from Oak Cliff](images/dallas-skyline-day.jpg) | 3494 × 592 | Cordphaeton · [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0) | [Source](https://commons.wikimedia.org/wiki/File:Downtown_Dallas_from_Belmont_Hotel_in_Oak_Cliff,_1.jpg) |
| [Freiburg — Schlossberg panorama](images/freiburg-schlossberg-panorama.jpg) | 7725 × 1000 | A. Hornung · [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0) | [Source](https://commons.wikimedia.org/wiki/File:Freiburg_Panorama_1000.jpg) |
| [Freiburg — city and wooded hills](images/freiburg-city-and-hills.jpg) | 3840 × 2553 | joergens.mi · [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0) | [Source](https://commons.wikimedia.org/wiki/File:View_(Freiburg_im_Breisgau)_jm10128.jpg) |
| [Marseille — your Calanques panorama](images/marseille-calanques.jpg) | 6080 × 1671 | Existing photograph supplied through Elías’s website · User-supplied existing website asset; photographer credit to confirm | [Source](https://elias-cisneros.com/research/) |
| [Quito — historic center and basilica](images/quito-historic-center-basilica.jpg) | 3840 × 2379 | Cayambe · [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0) | [Source](https://commons.wikimedia.org/wiki/File:Quito_as_from_panecillo_Basilica.jpg) |
| [Quito — historic center and Andes panorama](images/quito-historic-center-panorama.jpg) | 3840 × 833 | Diego Delso · [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) | [Source](https://commons.wikimedia.org/wiki/File:Vista_de_Quito_desde_El_Panecillo,_Ecuador,_2015-07-22,_DD_25-29_PAN.JPG) |

## Crop notes

- **Dallas — skyline at dusk:** A warm skyline silhouette at dusk. Strong contrast and room for white text.
- **Dallas — skyline from Oak Cliff:** A very wide daylight skyline from Oak Cliff. Works best as a shallow panoramic strip.
- **Freiburg — Schlossberg panorama:** A view from the Schlossberg tower with Freiburg below and wooded mountains to the side. The crop favors the mountain and city together.
- **Freiburg — city and wooded hills:** A closer view of the Münster against the wooded Schlossberg; stronger green detail, with less of the wider city.
- **Marseille — your Calanques panorama:** Your existing Research-page image. Its natural 3.64:1 shape already suits a wide banner.
- **Quito — historic center and basilica:** The clearest historic-center option: the basilica and dense colonial roofscape remain recognizable in a wide crop.
- **Quito — historic center and Andes panorama:** An expansive city-and-mountain view from El Panecillo; historic-center landmarks are smaller than in the basilica view.

## Credits and provenance

For Commons images, retain the author credit, source link, and license link, and identify a crop if a derivative is published. The CC BY-SA license applies to the image and its adaptations. `sources.json` preserves each source page, original file URL, downloaded dimensions, and the initial preview crop.

The Marseille image is copied without modification from `/Users/eliascis/Dropbox/omagua/web/eliascis.github.io/assets/images/IMG_20180519_162919.jpg`, the exact `header.overlay_image` in `_pages/research.md`. Its use here was requested by Elías. The photographer credit is not specified in that header.

Two initial Quito rooftop/cloud studies remain in `images/` and `sources.json` as non-shortlisted exploratory downloads.

## Local viewing

Open `preview.html` directly in a browser, or run from this directory:

```sh
python3 -m http.server 8766 --bind 127.0.0.1
```

Then visit <http://127.0.0.1:8766/preview.html>.
