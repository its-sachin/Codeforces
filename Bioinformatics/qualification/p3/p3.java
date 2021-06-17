import java.util.Scanner;
import java.util.ArrayList;
import java.util.HashMap;
import java.io.File;
import java.io.IOException;
import java.io.FileWriter;


class p3{

    public static void main(String[] args) {

        File file = new File(args[0]);

        try {

            try {
                FileWriter ans = new FileWriter("ans.txt");

                Scanner scn = new Scanner(file);
                int n = scn.nextInt();

                Tree body = new Tree(n);

                for (int i=2; i<=n; i++){
                    int p = scn.nextInt();
                    body.setParent(i,p);
                }

                for (int i=1; i<=n; i++){
                    int v = scn.nextInt();
                    body.setVal(i,v);
                }

                body.setHeight(1,0);

                int m = scn.nextInt();
                ArrayList<Integer>[] Dm = new ArrayList[m];

                for (int i=0; i<m; i++) {
                    Dm[i] = new ArrayList<Integer>();
            
                    int dm = scn.nextInt();
            
                    for (int j=0; j<dm; j++){
                        Dm[i].add(scn.nextInt());
                    }
                    
                }

                int p = scn.nextInt();
                ArrayList<Integer>[] Qp = new ArrayList[p];

                for (int i=0; i<p; i++) {
                    Qp[i] = new ArrayList<Integer>();
            
                    int qp = scn.nextInt();
            
                    for (int j=0; j<qp; j++){
                        Qp[i].add(scn.nextInt());
                    }
                    
                }


                // for (int i=1; i<=n; i++) {
                    
                //     System.out.println("height of " + i+ " " + body.getHeight(i) );
                // } 

                for (int i=0; i<p; i++){
                    System.out.println("PATIENTS LEFT " + Integer.toString(p-i) );

                    int maxVal = Integer.MIN_VALUE;
                    int diesease = 0;

                    for (int j=0; j<m; j++) {

                        int sum =0;
                
                        for (int k =0; k<Qp[i].size(); k++){
                
                            int maxIC = Integer.MIN_VALUE;
                
                            for (int l=0; l<Dm[j].size(); l++){
                                // System.out.println(i + " " + j + " " + k + " " + l + " " + Qp[i].get(k) + " " + Dm[j].get(l));
                                
                                int currIC = body.getLCA(Qp[i].get(k),Dm[j].get(l));
                                // System.out.println(currIC);
                                if (currIC > maxIC){
                                    maxIC = currIC;
                                }
                            }
                
                            sum+=maxIC;
                
                        }
                
                        if (maxVal<sum){
                            maxVal = sum;
                            diesease = j;
                        }
                
                    }

                    ans.write(Integer.toString(diesease+1)+"\n");
                }
                ans.close();
            
            }
            
            catch (IOException e) {
                System.out.print("in");
                return;
            }
        }
        
        catch (Exception e) {
            System.out.print("out");
            return;
        }
        

        
    }

}

class Vertex{
    
    public int val;
    public int parent;

    public int height;
    public ArrayList<Integer> childs;

    Vertex(){
        val = 0;
        parent = 1;
        height = 0;
        childs = new ArrayList<>();
    }
    
}
    
    
class Tree{

    public int N;
    public Vertex[] vertices;
    public HashMap<Integer,HashMap<Integer,Integer>> lcaVal;


    public Tree(int n){
        N=n;
        vertices = new Vertex[n];
        for (int i=0; i<n ;i++){
            vertices[i]=new Vertex();
        }
        lcaVal = new HashMap<>();
    }

    public void setVal(int vertex, int v){
        vertices[vertex-1].val = v;
    }
    
    public void setParent(int child, int parent){

        vertices[child-1].parent = parent;
        vertices[parent-1].childs.add(child);
    }

    public void setHeight(int currV, int height){

        vertices[currV-1].height = height;

        for (int i=0; i< vertices[currV-1].childs.size(); i++){
            setHeight(vertices[currV-1].childs.get(i),height+1);
        }
        
    }

    public int lca(int q, int d){

        if (q==d){
            return q;
        }

        if (vertices[q-1].height >= vertices[d-1].height){
            if (d==1){
                return 1;
            }

            return getAncestor(q,d);
        }

        else{
            if (q==1){
                return 1;
            }

            return getAncestor(d,q);
        }

    }

    public int getAncestor(int child, int parent){

        if (vertices[child-1].height == vertices[parent-1].height){
        
            if (vertices[child-1].parent == vertices[parent-1].parent){
                return vertices[child-1].parent;
            }

            int p1 = vertices[child-1].parent;
            int p2 = vertices[parent-1].parent;

            while(true){

                if (p1==p2){
                    return p1;
                }

                p1 = vertices[p1-1].parent;
                p2 = vertices[p2-1].parent;

            }
        }
        
        else{
            return getAncestor(vertices[child-1].parent,parent);
        }
    }

    public int getHeight(int vertex){
        return vertices[vertex-1].height;
    }

    public int getVal(int vertex){
        return vertices[vertex-1].val;
    }

    public int getParent(int vertex){
        return vertices[vertex-1].parent;
    }


    public int getLCA(int i, int j){

        // if (lcaVal.containsKey(i) && lcaVal.get(i).containsKey(j)){
        //     return vertices[lcaVal.get(i).get(j)-1].val;
        // }
        int l = lca(i,j);
        
        
        // if (!lcaVal.containsKey(i)){
        //     HashMap<Integer,Integer> t1 = new HashMap<>();
        //     t1.put(j,l);
        //     lcaVal.put(i,t1);
        // } 
        // else{
        //     lcaVal.get(i).put(j,l);
        // }

        // if (!lcaVal.containsKey(j)){
        //     HashMap<Integer,Integer> t1 = new HashMap<>();
        //     t1.put(i,l);
        //     lcaVal.put(j,t1);
        // } 
        // else{
        //     lcaVal.get(j).put(i,l);
        // }

        return vertices[l-1].val;
    }

    
}

