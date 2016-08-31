
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.Set;
import java.util.TreeSet; 

/**
 * Axel Mazariegos 131212
 * Julio Merida 15242
 * Gustavo Orellana 15073
 */
public class FactorySET {
    
    public Set ObtenerSET (String opcion) {
        
        if (opcion.equals("hashset")){ 
            return new HashSet(); 
        }

        if (opcion.equals("treeset")){
            return new TreeSet(); 
        }

        if (opcion.equals("linkedhashset")){ 
            return new LinkedHashSet(); 
        }

        return null;
    }
    
}
