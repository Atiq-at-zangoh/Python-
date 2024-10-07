
# LISTS

social_media = ['Twitter', 'Instagram', 'Threads', 'Facebook', 'LinkedIn']

print(*social_media)

print(social_media, sep=' ')

social_media.insert(0, "X")
print(*social_media)

social_media.pop(3)
print(*social_media)

social_media.append("Insta")
print(*social_media)

social_media.extend(['WhatsApp', 'Telegram', 'Discord'])
print(*social_media)

del social_media[3]
print(*social_media)