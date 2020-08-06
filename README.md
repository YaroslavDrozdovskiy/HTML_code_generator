# Генератор html кода 
______
* В коде присутствуют три основных класса HTML, TopLevelTag и Tag, вызываемые контекстным менеджером with
* Класс HTML определяет, куда сохранять вывод: на экран через print, или в файл, если передан именованный аргумент output = 'output.txt'

# Пример
Следующий код
```python
with HTML
     with TopLevelTag("body") as body:
          with Tag("div") as div:
              with Tag("p") as paragraph:
                  paragraph.text = "Какой-то текст"
                  div.children.append(paragraph)

              body.children.append(div)
```
Выведет в консоль или сохранит в файл html
```HTML
<html>
     <body>
      <div>
       <p>Какой-то текст</p>
      </div>
     </body>
<html>
```
