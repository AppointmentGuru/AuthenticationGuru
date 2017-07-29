## Kong Oauth

This library includes all the things you need to use Kong OAuth with the client credentials flow and Django.

### Getting started

```
pip install kong-oauth
```

Add to `INSTALLED_APPS` in settings: `kong_oauth`

Add urls:

```
url(r'^', include('kong_oauth.urls')),
```

You'll also need to set the following settings:

* `KONG_OAUTH_ENDPOINT`
* `KONG_ADMIN_URL`
* `KONG_GATEWAY_URL`
* `KONG_ADMIN_USERNAME`
* `KONG_ADMIN_PASSWORD`
* `KONG_PROVISION_KEY`




### Add middleware

(this middleware will make a user available on `request.user` with the id of the authenticated user as per: `HTTP_X_AUTHENTICATED_USERID`).

This is so that upstream services from Kong can deal with the active user. These servers should not be available except via Kong (for obvious reasons)

```
MIDDLEWARE = [
    'kong_oauth.middleware.KongUserMiddleware'
]
```


