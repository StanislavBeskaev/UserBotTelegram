#!/bin/bash
docker run --rm -dit --env-file .env -v $(pwd):/user_bot user_bot