from django.shortcuts import render, HttpResponse


# Create your views here.


def index(request):
    html = '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Main</title>
</head>
<body>
<h1 class="h1-style">Главная страница</h1>
<p class="p-style">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad alias eveniet id magni quae quisquam tempora temporibus?
    Eius est et ipsa provident, quibusdam quo rerum sunt totam voluptatum? Aperiam dolore est eveniet harum inventore,
    itaque ratione tempora veritatis! Aspernatur at illum maiores minus nobis numquam rerum sit temporibus ut!
    Accusantium cum, debitis dignissimos dolorem est excepturi obcaecati odit officia, officiis, quas qui repellendus
    vero voluptatibus. Ad alias aliquid consectetur cumque distinctio dolorem doloremque eum necessitatibus nulla porro
    quam qui, quisquam quo recusandae reiciendis sint unde veritatis vero! Ab commodi enim, excepturi maiores, natus
    officiis perferendis quo sint tempora, vero voluptatibus.
</p>
<h2 class="h2-style">Добро пожаловать на сайт</h2>
<p class="p-style">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cupiditate dolor dolore dolorem earum et itaque natus
    officia repudiandae unde. Molestias.
</p>
<p class="p-style">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cupiditate dolor dolore dolorem earum et itaque natus
    officia repudiandae unde. Molestias.
</p>
<p class="p-style">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cupiditate dolor dolore dolorem earum et itaque natus
    officia repudiandae unde. Molestias.
</p>

</body>
</html>
    '''

    return HttpResponse(html)


def about(request):
    html = '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Main</title>
    </head>
    <body>
    <h1 class="h1-style">Вот что я могу рассказать о себе</h1>
    <p class="p-style">id neque aliquam vestibulum morbi blandit cursus risus at ultrices mi tempus imperdiet nulla
    malesuada pellentesque elit eget gravida cum sociis natoque penatibus et magnis dis parturient montes nascetur
    ridiculus mus mauris vitae ultricies leo integer malesuada nunc vel risus commodo viverra maecenas accumsan
    lacus vel facilisis volutpat est velit egestas dui id ornare arcu odio ut sem nulla pharetra diam sit amet nisl
    suscipit adipiscing bibendum est ultricies integer quis auctor elit sed vulputate mi sit amet mauris commodo quis
    imperdiet massa tincidunt nunc pulvinar sapien et ligula ullamcorper malesuada proin libero nunc consequat interdum
    varius sit amet mattis vulputate enim nulla aliquet porttitor lacus luctus accumsan tortor posuere ac ut consequat
    semper viverra nam libero justo laoreet sit amet cursus sit amet dictum sit amet justo donec enim diam vulputate u 
    pharetra sit amet aliquam id diam maecenas ultricies mi eget mauris pharetra et ultrices neque ornare aenean euismod
    elementum nisi quis eleifend quam adipiscing vitae proin sagittis nisl rhoncus mattis rhoncus urna neque viverra
    justo nec ultrices dui sapien eget mi proin sed libero enim sed faucibus turpis in eu mi bibendum neque egestas
    congue quisque egestas diam in arcu cursus euismod quis viverra nibh cras pulvinar
    </p>
    <h2 class="h2-style">А вот рассказ о том как я содал первое приложение Django</h2>
    <p class="p-style">aliquam nulla facilisi cras fermentum odio eu feugiat pretium nibh ipsum consequat nisl vel
    pretium lectus quam id leo in vitae turpis massa sed elementum tempus egestas sed sed risus pretium quam vulputate
    dignissim suspendisse in est ante in nibh mauris cursus mattis molestie a iaculis at erat pellentesque adipiscing
    commodo elit at imperdiet dui accumsan sit amet nulla facilisi morbi tempus iaculis urna id volutpat lacus laoreet
    non curabitur gravida arcu ac tortor dignissim convallis aenean et tortor at risus viverra adipiscing at in tellus
    integer feugiat scelerisque varius morbi enim nunc faucibus a pellentesque sit amet porttitor eget dolor morbi non
    arcu risus quis varius quam quisque id diam
    </p>
    </body>
    </html>
        '''

    return HttpResponse(html)
