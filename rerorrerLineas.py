a="""
    public CapasitacionEstudiante createAndGet(CapasitacionEstudiante capasitacionestudiante)throws Exception{
        String inputJson = null;
        inputJson = JSONUtils.covertFromObjectToJson(capasitacionestudiante);
        HttpRequest request = HttpRequest.newBuilder(URI.create(serviceURL+"create"))
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(inputJson)).build();
        CompletableFuture<HttpResponse<String>> response = client.sendAsync(request,HttpResponse.BodyHandlers.ofString());
        capasitacionestudiante=null;
        try {
            //pq por encima de este numero es una peticion incorrecta
            if(response.get().statusCode() > 299){
                response.join();
                return null;
            }else {
                try {
                    capasitacionestudiante = JSONUtils.covertFromJsonToObject(response.get().body(), CapasitacionEstudiante.class);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                } catch (ExecutionException e) {
                    e.printStackTrace();
                }
                response.join();
                return capasitacionestudiante;
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
            
        } catch (ExecutionException e) {
            e.printStackTrace();
            
        }
        return capasitacionestudiante;
    }

"""
def r(metodo):
	global a
	l=a.split('\n')
	for v in l:
		if len(v.strip())>0:
			print(metodo(v))


def contar_tabulaciones(texto):
    """
    Retorna la cantidad de tabulaciones con la que comienza el texto.
    """
    espacios = 0
    contador = 0
    for caracter in texto:
        if caracter == '\t':
            contador += 1
        elif caracter == " ":
            espacios += 1
            if espacios == 4:
                contador += 1
                espacios = 0
        else:
            break
    return contador


def eliminar_tabulaciones(texto):
    """
    Retorna el texto sin las tabulaciones con las que comienza.
    """

    contador = 0
    for caracter in texto:
        if caracter == '\t':
            contador += 1
        if caracter == " ":
            contador += 1
        else:
            break
    return texto[contador:]


def sp(v):
	c=contar_tabulaciones(v)
	if c>0:
		return str(c)
	return ""
def pr(v):
	v=eliminar_tabulaciones(v)
	v=v.replace('"','\\"')
	return v
r(lambda v:'mr += separacion'+sp(v)+' + "'+pr(v)+'";')