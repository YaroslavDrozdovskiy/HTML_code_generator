# Генератор html кода 
______
* В коде присутствуют три основных класса HTML, TopLevelTag и Tag, вызываемые контекстным менеджером with
* Класс HTML определяет, куда сохранять вывод: на экран через print, или в файл, если передан именованный аргумент output = 'output.txt'

# Пример
```python
with Tag("body", toplevel=True) as body:
     with Tag("div") as div:
         with Tag("p") as paragraph:
             paragraph.text = "Какой-то текст"
             div.children.append(paragraph)

         body.children.append(div)
```
