frutas_vermelhas = {"banana"}
novas_frutas_vermelhas = {"morango", "cereja", "framboesa"}

frutas_vermelhas.update(novas_frutas_vermelhas)

frutas_vermelhas.discard("cereja")

print(frutas_vermelhas)
