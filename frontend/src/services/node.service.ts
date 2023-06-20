import { api } from 'boot/axios';
import { GetNodeReponse, GetNodesLengthResponse } from 'src/models/node.model';
import { Node } from 'src/models/node.model';
import { useNodeStore } from 'src/stores/node-store';

export class NodeService {
  private nodeStore;

  constructor() {
    this.nodeStore = useNodeStore();
  }

  async setCurrentNode(node: Node | undefined): Promise<void> {
    this.nodeStore.currentNode = node;

    // get immediate neighbors
    const neighbors = [];
    if (node) {
      for (const neighborId of node.neighbors) {
        const node = await this.getNodeById(neighborId);
        neighbors.push(node);
      }
    }
    this.nodeStore.currentNeighbors = neighbors;
  }

  async getRandomNode(): Promise<Node> {
    const resp = (await api.get('nodes/random')) as GetNodeReponse;
    return resp.data;
  }

  async getNodeById(id: number): Promise<Node> {
    const resp = (await api.get(`nodes/${id}`)) as GetNodeReponse;
    return resp.data;
  }

  async getNodeQty(): Promise<void> {
    const resp = (await api.get('nodes/length')) as GetNodesLengthResponse;
    this.nodeStore.nodeQty = resp.data ? resp.data : 0;
  }

  async deleteAllNodes(): Promise<void> {
    await api.delete('nodes');
  }

  async generateNodes(): Promise<void> {
    await api.post('nodes');
  }
}
