a="""

    public Users findById(int id) {
        Users user = null;
        HttpRequest req = HttpRequest.newBuilder(URI.create(serviceURL+"find/"+id)).GET().build();
        CompletableFuture<HttpResponse<String>> response = client.sendAsync(req, HttpResponse.BodyHandlers.ofString());
        try {
            if(response.get().statusCode() == 500){
                response.join();
                return null;
            }else {

                try {
                    user = JSONUtils.covertFromJsonToObject(response.get().body(), Users.class);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                } catch (ExecutionException e) {
                    e.printStackTrace();
                }
                response.join();
                return user;
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (ExecutionException e) {
            e.printStackTrace();
        }
        return user;
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