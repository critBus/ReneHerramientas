a="""

import Entity.Users;
import Utils.JSONUtils;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.core.type.TypeReference;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;

public class RestUsers {

    private static final HttpClient client = HttpClient.newBuilder().version(HttpClient.Version.HTTP_2).build();
    private static final String serviceURL = "http://localhost:8081/Users/";

    //sending request to retrieve all users available.
    public List<Users> findAllUsers() {
        HttpRequest req = HttpRequest.newBuilder(URI.create(serviceURL+"findAll")).GET().build();
        CompletableFuture<HttpResponse<String>> response = client.sendAsync(req, HttpResponse.BodyHandlers.ofString());
        List<Users> list_users = null;
        try {
            list_users = JSONUtils.convertFromJsonToList(response.get().body(), new
                    TypeReference<List<Users>>() {});
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (ExecutionException e) {
            e.printStackTrace();
        }
        response.join();
        return list_users;
    }

    

    //send request to add the product details.
    public boolean createUser(Users user){
        String inputJson = null;
        inputJson = JSONUtils.covertFromObjectToJson(user);
        HttpRequest request = HttpRequest.newBuilder(URI.create(serviceURL+"create"))
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(inputJson)).build();
        CompletableFuture<HttpResponse<String>> response = client.sendAsync(request,HttpResponse.BodyHandlers.ofString());
        try {
            if(response.get().statusCode() == 500){
                return false;
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
            return false;
        } catch (ExecutionException e) {
            e.printStackTrace();
            return false;
        }
        return true;
    }

    //send request to update a User details.
    public boolean updateUser(Users user){
        String inputJson= null;
        inputJson = JSONUtils.covertFromObjectToJson(user);
        HttpRequest request = HttpRequest.newBuilder(URI.create(serviceURL+"update"))
                .header("Content-Type", "application/json")
                .PUT(HttpRequest.BodyPublishers.ofString(inputJson)).build();
        CompletableFuture<HttpResponse<String>> response = client.sendAsync(request,HttpResponse.BodyHandlers.ofString());
        try {
            if(response.get().statusCode() == 500){
                response.join();
                return false;
            } else {
                user = JSONUtils.covertFromJsonToObject(response.get().body(), Users.class);
                response.join();
                return true;
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (ExecutionException e) {
            e.printStackTrace();
        }
        return false;
    }

    //send request to delete the user by its username
    public boolean deleteUser(String username) {
        HttpRequest request = HttpRequest.newBuilder(URI.create(serviceURL+"delete/"+username)).DELETE().build();
        CompletableFuture<HttpResponse<String>> response = client.sendAsync(request,HttpResponse.BodyHandlers.ofString());
        try {
            if(response.get().statusCode() == 500) {
                response.join();
                return false;
            } else {
                Users user = JSONUtils.covertFromJsonToObject(response.get().body(), Users.class);
                response.join();
                return true;
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (ExecutionException e) {
            e.printStackTrace();
        }
        return false;
    }

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