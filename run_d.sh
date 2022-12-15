#!/bin/bash
docker run -dit --env-file .env -v $(pwd):/user_bot user_bot