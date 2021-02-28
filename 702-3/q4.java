import java.util.*;

public class q4{
    public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

        int numTestCases = sc.nextInt();

        while(numTestCases-->0){
            int n = sc.nextInt();
            int[] array = new int[n];

            Tree t = new Tree();

            for(int i=0; i<n; i++){
                array[i] = sc.nextInt();
                t.insert(t.root,new Node(array[i]));
            }

            for(int i=0; i<n; i++){
                System.out.println()
            }


        }
    }

    
}

class Node{
    int val;
    int height;
    Node left;
    Node right;
    Node parent;

    public Node(int val){
        this.val = val;
        this.height = 0;
    }
}

class Tree{
    Node root;

    public void insert(Node r, Node n){
        if (r.val < n.val) {
            n.left = r;
            if (root == r){
                root = n;
                n.height =0;
            }
            else {
                r.parent.right = n;
                n.height= r.height;
                Node curr = r.right;
                while(r != null){
                    r.height += 1;
                    r = r.left;
                }
                while(curr != null){
                    curr.height += 1;
                    curr = curr.right;
                }
            }

        }

        else {
            if (r.right == null) {
                r.right = n;
                n.parent = r;
                n.height = r.height + 1;
            }
            else {
                insert(r.right,n);
            }
        }
    }

    // CheckBalance function maintains the height balanced property and perform desired rotations.
    
}
