# Project Dockerization
## Authors
- Emelda Honba Wogse (charlene.honba-wogse@epita.fr)
- Samuel Goncalves (samuel.goncalves@epita.fr)
## Prerequis command
- stage2:
    - `docker volume create --opt type=tmpfs --opt device=tmpfs --opt o=size=8g sepia-volume`
    - `docker run --rm -v monvolume:/volume busybox chmod ugo+rwxt /volume`
