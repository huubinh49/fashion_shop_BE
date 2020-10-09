function DFS(list, vertex, graph, visited){
    if(!visited[vertex]){
        list.push(vertex);
        visited[vertex] = true;
    }
    for(let i = 0; i<graph[vertex].length;i++){
        let u = graph[vertex][i];

        if(!visited[u]){
            DFS(list, u, graph, visited);
        }
    }
}
function covidSeverity(n,a,b){
    // n => số người 
    // a => mảng liên kết
    // b => những người F0

    let graph = new Array(n+1).fill(null).map(item=>[]);
    let visited = new Array(n+1).fill(false);
    for(let i =0; i<a.length;i++){
        graph[a[i][0]].push(a[i][1])
        graph[a[i][1]].push(a[i][0])
    }
    let components = [];
    for(let i = 1; i<= n;i++){
        if(!visited[i]){
            let list = [];
            DFS(list, i, graph, visited);
            components.push(list);
        }
    }

    let covid = new Array(n+1).fill(0).map((item, key)=>{
        if(b.findIndex(item=> item==key)!=-1)
        return 0;
        return -1;
    });
    

    let result = [];
    for(let component of components){
        let covidComponent = 0;
        for(let u of component){
            if(covid[u]==0){
                visited = visited.fill(false);
                DFSCovid(component, covid, u, graph, visited);
            }
            
        }
        for(let u of component){
            switch (covid[u]) {
                case 0:
                    covidComponent+=10;
                    break;
                case 1:
                    covidComponent+=5;
                    break;
                case 2:
                    covidComponent+=3;
                    break;
                    
                case 3:
                    covidComponent+=1;
                    break;
                    
                default:
                    covidComponent+=0;
                    break;
            }
        }
        result.push(covidComponent);
    }
    console.log(covid)
    return result.sort((a, b)=> b-a);
}
function DFSCovid(component, covid, vertex, graph, visited) {
        let queue = [vertex];
        while(queue.length){
            let s = queue.shift();
            for(let u of graph[s]){
                if(!visited[u]){
                    visited[u]=true;
                    if(covid[u]==-1){
                        covid[u] = (covid[s]!=3)? covid[s]+1 : covid[s];
                    }else
                    covid[u] = Math.min(covid[u],  (covid[s]!=3)? covid[s]+1 : covid[s])
                    queue.push(u)
                }
            }
        }
        
}

console.log(covidSeverity(6,[[1,6],[5,1],[6,4],[4,3],[5,3]],[4,3]))