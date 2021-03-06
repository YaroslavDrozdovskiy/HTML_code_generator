# Генератор html кода 
______
* В коде присутствуют три основных класса HTML, TopLevelTag и Tag, вызываемые контекстным менеджером with
* Класс HTML определяет, куда сохранять вывод: на экран через print, или в файл, если передан именованный аргумент output = 'output.txt'

# Пример
```python
with HTML(output="test.html") as doc:
    with TopLevelTag("head") as head:
        with Tag("title") as title:
            title.text = "hello"
            head += title
        doc += head

    with TopLevelTag("body") as body:
        with Tag("h1", klass=("main-text",)) as h1:
            h1.text = "Test"
            body += h1

        with Tag("div", klass=("container", "container-fluid"), id="lead") as div:
            with Tag("p") as paragraph:
                paragraph.text = "another test"
                div += paragraph

            with Tag("img", is_single=True, src="/icon.png" data_image="responsive") as img:
                div += img

            body += div

        doc += body
```
Выполенный код сохранит результат в файл test.html
```HTML
<html>
<head>
  <title>hello</title>
</head>
<body>
    <h1 class="main-text">Test</h1>
    <div class="container container-fluid" id="lead">
        <p>another test</p>
        <img src="/icon.png" data-image="responsive"/>
    </div>
</body>
</html>
```
