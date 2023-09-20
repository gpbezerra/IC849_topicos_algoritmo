// Adicionar um novo vertice no grafo, verificando se ele já existe
// Adicionar um aresta referenciando destino e  raiz
// Criar vertice, adicionar vizinho, remover vizinho
// Criar grafo, adicionr novo vertice, remover vertice, adicionar e remover aresta

class Vertex {
    public id: number;
    public adjNodes: Vertex[];
    public color?: string;
    
    constructor(id: number) {
        this.id = id;
        this.adjNodes = new Array();
    }

    public getID(): number{
        return this.id;
    }

    public setId(id: number){
        this.id = id;
    }

    public getAdjNodes(): Vertex[]{
        return this.adjNodes;
    }

    public setAdjNodes(adjNodes: Vertex[]){
        this.adjNodes = adjNodes;
    }
}

class Graph {
    public nodes: Vertex[];
    public type?: string;

    constructor(){
        this.nodes = new Array();
    }

    public addNode(node: Vertex): boolean{

        // Verficando se ele já existe
        if(this.nodes.find(element => element.id == node.id)) {
            return true;
        }
        this.nodes.push(node);
        return true;
    }

    public addEdge(node1: Vertex, node2: Vertex){
        
        // Repensar numa forma melhor de verficar e atribuir direto os vertices adjacente de cada vertice
        
        if(this.nodes.find(element => element.id == node1.id)) {

            // Verficar se os vertices já são vizinhos
            if (node1.adjNodes.find(node => node.id === node2.id) == null) {
                node1.adjNodes.push(node2);
                return true;
            } else {
                return true;
            }
        }

        if(this.nodes.find(element => element.id == node2.id)) {
            if (node2.adjNodes.find(node => node.id === node1.id) == null) {
                node2.adjNodes.push(node1);
                return true;
            } else {
                return true;
            }
        }

    }

    public removeNode(node: Vertex): Vertex[]{
        this.nodes = this.nodes.filter(element => element.id != node.id)
        return this.nodes;
    } 

    public removeEdge(node1: Vertex, node2: Vertex){
    }
}

    