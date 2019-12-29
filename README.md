# rooking-api

This is the Rooking REST API

## Docker image build:

```bash
docker build -t rooking-api .
```

## Docker container start:

```bash
docker run --rm -d --name=rooking-api -p 5000:5000 rooking-api
```

## Available Methods:

| HTTP Method | URI                                        | Action                  |
| ----------: | ------------------------------------------ | ----------------------- |
|         GET | http://[hostname]/api/v1.0/rooms           | Retrieve list of rooms  |
|         GET | http://[hostname]/api/v1.0/rooms/[room_id] | Retrieve a room         |
|        POST | http://[hostname]/todo/api/v1.0/rooms      | Create a new room       |
|         PUT | http://[hostname]/api/v1.0/rooms/[room_id] | Update an existing room |
|      DELETE | http://[hostname]/api/v1.0/rooms/[room_id] | Delete a room           |

## Examples

> Adding a new room:
>
> ```bash
> curl -i -H "Content-Type: application/json" -X POST -d '{"title":"La Tranquera"}' > http://localhost:5000/api/v1.0/rooms
> ```

> Updating a room:
>
> ```bash
> curl -i -H "Content-Type: application/json" -X PUT -d '{"available":false}' http://localhost:5000/api/v1.0/rooms/2
> ```

> Deleting a room:
>
> ```bash
> curl -i -H "Content-Type: application/json" -X DELETE  http://localhost:5000/api/v1.0/rooms/2
> ```
