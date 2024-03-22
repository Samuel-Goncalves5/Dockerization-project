# Project Dockerization
## Authors
- Emelda Honba Wogse (charlene.honba-wogse@epita.fr)
- Samuel Goncalves (samuel.goncalves@epita.fr)
## Prerequis command
- stage1:
    - `docker compose up`
- stage2:
    # Terminal 1
    - `docker volume create --opt type=tmpfs --opt device=tmpfs --opt o=size=8g sepia-volume`
    - `docker run --rm -v monvolume:/volume busybox chmod ugo+rwxt /volume`
    - `docker compose up`
    # Terminal 2
    - `docker run --rm -i -v=sepia-volume:/tmp/myvolume busybox find /tmp/myvolume`
