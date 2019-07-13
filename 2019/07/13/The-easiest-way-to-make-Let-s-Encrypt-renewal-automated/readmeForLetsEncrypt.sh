  #!/bin/bash
  now="$(date)"
  printf "Current date and time %s\n" "$now"
  cd letsencrypt/; ./letsencrypt-auto renew