<template>
  <div class="row">
    <div class="q-mb-lg">
      <q-btn
        :disable="previousNodes.length === 0"
        class="q-mx-md"
        color="primary"
        label="Back"
        @click="$emit('goBack')"
      />
      <q-btn
        :disable="nodeStore.nodeQty === 0"
        class="q-mr-md"
        color="primary"
        label="Random"
        @click="$emit('gotoRandom')"
      />
      <q-btn
        class="q-mr-md"
        color="positive"
        label="Generate Nodes"
        @click="$emit('generateNodes')"
      />
      <q-btn
        :disable="nodeStore.nodeQty === 0"
        class="q-mr-md"
        color="negative"
        label="DELETE ALL"
        @click="$emit('deleteAllNodes')"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useNodeStore } from 'src/stores/node-store';
import { Node } from 'src/models/node.model';

export default defineComponent({
  name: 'NodeActionButtonRow',

  props: {
    previousNodes: {
      type: Array<Node>,
      required: true,
    },
  },

  emits: ['goBack', 'gotoRandom', 'generateNodes', 'deleteAllNodes'],

  setup() {
    return {
      nodeStore: useNodeStore(),
    };
  },
});
</script>
