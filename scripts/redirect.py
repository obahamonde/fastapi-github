from yaml import safe_load

with open('./deploy.yml') as f:
    data = safe_load(f)
    print(data)

with open('netlify.toml', 'w') as f:
    f.write(f"""[[redirects]]
    from = "/api/*"
    to = "{data['endpoint']}:splat"
    status = 200
    force = true
    """)
