# Project Dockerization
## Authors
- Emelda Honba Wogse (charlene.honba-wogse@epita.fr)
- Samuel Goncalves (samuel.goncalves@epita.fr)
## Prerequis command
- stage1:
    - `docker compose up`
- stage2:
    # Terminal 1
    - `docker run --rm -v sepia-volume:/volume busybox chmod ugo+rwxt /volume`
    - `docker compose up`
