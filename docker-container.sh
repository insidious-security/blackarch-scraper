#!/bin/bash
docker run -d -e POSTGRES_PASSWORD=password -e POSTGRES_USER=postgres -p 5432:5432 --name postgres-0 postgres
