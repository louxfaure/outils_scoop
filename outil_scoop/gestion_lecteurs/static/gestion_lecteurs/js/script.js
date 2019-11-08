function validateForm() {
    if (document.getElementsByClassName('alert')){
        var nodeAlert = document.getElementsByClassName('alert');
        for (var i = 0; i < nodeAlert.length; i++) {
            nodeAlert[i].remove()
        }
    }

    var x = document.forms["form_modif_lecteur"]["nouvel_identifiant"];
    var y = document.forms["form_modif_lecteur"]["date_expiration"];
    if (x.value == "" && y.value == "") {
        alertmessage("Vous devez renseigneer au moins un champ !")
        x.classList.add('is-invalid');
        y.classList.add('is-invalid');
      return false;
    }
    else if (y.value != ""){
        var myDate = new Date(y.value);
        var today = new Date();
        if ( myDate < today ) {
            y.classList.add('is-invalid'); 
            alertmessage("La date de fin de validité doit être antérieure à celle du jour.")
            return false;
        }
        return true;
    }
    else{
        return true; 
    }
  } 

function alertmessage(message){
    var strongelement = document.createElement("strong");
    var strongelementContent = document.createTextNode("Saperlipopette ! ");
    strongelement.appendChild(strongelementContent);
    var invalidFeedbackNode = document.createElement("div");
    invalidFeedbackNode.classList.add('alert');
    invalidFeedbackNode.classList.add('alert-danger');
    invalidFeedbackNode.setAttribute('role','alert')
    var invalidFeedbackContent = document.createTextNode(message);
    invalidFeedbackNode.appendChild(strongelement);
    invalidFeedbackNode.appendChild(invalidFeedbackContent);
    var currentDiv = document.getElementsByTagName('button')[0].parentNode;
    var parentDiv = currentDiv.parentNode;
    parentDiv.insertBefore(invalidFeedbackNode, currentDiv);
}

