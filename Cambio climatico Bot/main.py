import discord
from discord.ext import commands


# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
intents.message_content = True

# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send("Hola! Estoy aquí para ayudarte a aprender más sobre el cambio climático.")

    elif message.content.startswith('$cambio-climatico'):
        mensaje = "**¿Qué es el cambio climático?**\n" \
                  "El cambio climático es el conjunto de cambios en el clima terrestre atribuidos principalmente a las actividades humanas, como la quema de combustibles fósiles, que aumentan la cantidad de gases de efecto invernadero en la atmósfera. Estos gases atrapan el calor y provocan un calentamiento gradual del planeta.\n" \
                  "**¿Cuáles son las causas del cambio climático?**\n" \
                  "La principal causa del cambio climático es la emisión de gases de efecto invernadero, como el dióxido de carbono, el metano y el óxido nitroso, a la atmósfera. Estas emisiones provienen principalmente de la quema de combustibles fósiles, la deforestación y la agricultura.\n" \
                  "**¿Cuáles son los efectos del cambio climático?**\n" \
                  "Los efectos del cambio climático son ya visibles y se están volviendo más intensos y frecuentes. Entre ellos se encuentran: el aumento de la temperatura global, el aumento del nivel del mar, la intensificación de los fenómenos meteorológicos extremos, la acidificación de los océanos y la pérdida de biodiversidad.\n" \
                  "**¿Qué podemos hacer para combatir el cambio climático?**\n" \
                  "Hay muchas cosas que podemos hacer para combatir el cambio climático, como: reducir nuestras emisiones de gases de efecto invernadero, apoyar el uso de energías renovables, conservar la energía, reducir el consumo de carne, evitar la deforestación y plantar árboles.\n" \
                  "Si tienes más preguntas o quieres saber más sobre el cambio climático, no dudes en preguntarme!"
        await message.channel.send(mensaje)

    elif message.content.startswith('$consejos'):
        mensaje = "**Consejos para reducir tu huella de carbono:**\n" \
                  "- Utiliza el transporte público, la bicicleta o camina en lugar de usar el coche siempre que sea posible.\n" \
                  "- Apaga las luces y los aparatos electrónicos cuando no los estés utilizando.\n" \
                  "- Reduce el consumo de agua caliente y toma duchas más cortas.\n" \
                  "- Recicla y reutiliza los materiales siempre que puedas.\n" \
                  "- Consume alimentos locales y de temporada.\n" \
                  "- Reduce el consumo de carne y productos lácteos.\n" \
                  "- Planta árboles y apoya la reforestación.\n" \
                  "- Participa en iniciativas de activismo climático y educa a otros sobre el tema."
        await message.channel.send(mensaje)

    else:
        await message.channel.send("No reconozco ese comando. Intenta usar $hello, $cambio-climatico o $consejos.")

client.run('Token')  # Reemplaza TU_TOKEN_DE_DISCORD con tu token real
