#!/bin/bash
docker run --rm -it --env-file .env -v $(pwd):/user_bot user_bot