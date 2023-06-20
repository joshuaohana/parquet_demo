<template>
  <q-page>
    <div class="row">
      <div class="q-mt-md">
        <h5>Total Nodes: {{ nodeStore.nodeQty }}</h5>
      </div>
    </div>

    <node-action-button-row
      :previousNodes="previousNodes"
      @goBack="goBack"
      @gotoRandom="gotoRandomNode"
      @generateNodes="generateNodes"
      @deleteAllNodes="deleteAllNodes"
    />

    <div class="row" v-if="nodeStore.nodeQty === 0">
      <div class="q-my-md">
        <p>No Nodes Available</p>
      </div>
    </div>

    <div class="row">
      <div class="q-my-md">
        <node-component
          v-if="nodeStore.currentNode"
          :text="nodeStore.currentNode.id.toString()"
          rootNode
        />
      </div>
    </div>
    <div class="row neighbors">
      <node-component
        v-for="node in nodeStore.currentNeighbors"
        :key="node.id"
        :text="node.id.toString()"
        @click="selectNeighbor(node.id)"
      />
    </div>
  </q-page>

  <node-info-side-drawer />

  <node-history-side-drawer
    @gotoNode="gotoNode"
    :previousNodes="previousNodes"
  />
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { NodeService } from 'src/services/node.service';
import { Node } from 'src/models/node.model';
import { useNodeStore } from 'src/stores/node-store';

import NodeComponent from 'src/components/NodeComponent.vue';
import NodeActionButtonRow from 'src/components/NodeActionButtonRow.vue';
import NodeInfoSideDrawer from 'src/components/NodeInfoSideDrawer.vue';
import NodeHistorySideDrawer from 'src/components/NodeHistorySideDrawer.vue';

export default defineComponent({
  name: 'IndexPage',
  components: {
    NodeComponent,
    NodeActionButtonRow,
    NodeInfoSideDrawer,
    NodeHistorySideDrawer,
  },

  setup() {
    return {
      nodeService: new NodeService(),
      nodeStore: useNodeStore(),
      previousNodes: ref<Node[]>([]),
    };
  },
  mounted() {
    this.init();
  },
  methods: {
    async init() {
      this.previousNodes = [];
      const node = await this.nodeService.getRandomNode();
      void this.nodeService.setCurrentNode(node);
      void this.nodeService.getNodeQty();
    },
    async selectNeighbor(id: number) {
      if (this.nodeStore.currentNode) {
        this.previousNodes.unshift(this.nodeStore.currentNode);
      }
      this.nodeService.setCurrentNode(
        this.nodeStore.currentNeighbors.find((node) => node.id === id)
      );
    },
    goBack() {
      this.nodeService.setCurrentNode(this.previousNodes.shift());
    },
    async gotoRandomNode() {
      if (this.nodeStore.currentNode) {
        this.previousNodes.unshift(this.nodeStore.currentNode);
      }
      const node = await this.nodeService.getRandomNode();
      void this.nodeService.setCurrentNode(node);
    },
    async gotoNode(id: number) {
      const index = this.previousNodes.findIndex((node) => node.id === id);
      if (index !== -1) {
        // Remove all nodes before the desired node
        this.nodeService.setCurrentNode(this.previousNodes[index]);
        this.previousNodes.splice(0, index + 1);
      } else {
        // If the desired node is not found, fetch it
        this.nodeService.setCurrentNode(await this.nodeService.getNodeById(id));
      }
    },
    async deleteAllNodes() {
      await this.nodeService.deleteAllNodes();
      this.init();
    },
    async generateNodes() {
      await this.nodeService.generateNodes();
      this.init();
    },
  },
});
</script>
<style scoped lang="scss">
.neighbors {
  .node {
    margin: 0 10px;
  }
}
.q-page > .row {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px auto;
}
</style>
