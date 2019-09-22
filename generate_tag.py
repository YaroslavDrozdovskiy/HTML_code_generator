from hood import *

def main(output=None):
    with HTML(output=output) as doc:
        with TopLevelTag("head") as head:
            with Tag("title") as title:
                title.text = "hello"
                head += title
            doc += head

        with TopLevelTag("body") as body:
            with Tag("h1", class_=("main-text",)) as h1:
                h1.text = "Test"
                body += h1

            with Tag("div", class_=("container", "container-fluid"), id="lead") as div:
                with Tag("p") as paragraph:
                    paragraph.text = "another test"
                    div += paragraph

                with Tag("img", is_single=True, src="/icon.png", data_image="responsive") as img:
                    div += img

                body += div

            doc += body

if __name__ == '__main__':
    main()
