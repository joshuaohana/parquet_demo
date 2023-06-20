import { defineStore } from 'pinia';
import { Node } from 'src/models/node.model';

export const useNodeStore = defineStore('node', {
  state: (): INodeStore => ({
    currentNode: undefined,
    currentNeighbors: [],
    nodeQty: 0,
  }),
});

interface INodeStore {
  currentNode: Node | undefined;
  currentNeighbors: Node[];
  nodeQty: number;
}
