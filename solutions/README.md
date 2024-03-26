# Project Dockerization
## Authors
- Emelda Honba Wogse (charlene.honba-wogse@epita.fr)
- Samuel Goncalves (samuel.goncalves@epita.fr)
## Prerequis command
- stage1:
    - `docker compose up`
- stage2:
    - `docker run --rm -v sepia-volume:/volume busybox chmod ugo+rwxt /volume`
    - `docker compose up`
- stage3: (les poids sont créés dans le volume au premier container, puis lus dans les autres s'ils existent)
    - `docker run --rm -v ocr-volume:/volume busybox chmod ugo+rwxt /volume`
    - `docker compose up`
