const lineReader = require('line-reader');

// function createGraph(vertexes, edges) {
// 	const graph = {
// 		vertexes,
// 		edges
// 	}

// 	return graph;
// }

function readGraphFromFile(filePath) {
	let lineIndex = 0;
	let numberOfVertexes = 0;
	let numberOfEdges = 0;
	const edges = [];

	lineReader.eachLine(filePath, (line, last) => {
		lineIndex = lineIndex + 1; // start at line one

		console.log(`lineIndex = ${lineIndex}`);

		if (lineIndex === 1) {
			console.log(`numberOfVertexes = parseInt(line) = ${numberOfVertexes = parseInt(line)}`);
			numberOfVertexes = parseInt(line);
			return
		}

		if(lineIndex === 2) {
			console.log(`numberOfEdges = parseInt(line) = ${numberOfEdges = parseInt(line)}`);
			numberOfEdges = parseInt(line);
			return
		}

		if(lineIndex > numberOfEdges + 2) {
			// past the number of edges 
			console.log(`stop`);
			return false // stop the reading
		} else {
			// lines that represent the edges

			console.log(`line = ${line}`);

			let edgeVertexes = line.split(' ');

			edges.push({ v1: parseInt(edgeVertexes[0]), v2: parseInt(edgeVertexes[1]) });
			return
		}
	});

	setTimeout(() => {
		console.log(`numberOfVertexes = ${numberOfVertexes}`);
		console.log(`numberOfEdges = ${numberOfEdges}`);
		console.log(`JSON.stringify(edges) = ${JSON.stringify(edges)}`);
	}, 2000)
}

const graphFromFile = readGraphFromFile('./testGraph.txt');
