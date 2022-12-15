#!/bin/bash
docker run -it --env-file .env -v $(pwd):/user_bot user_bot