<template>
  <q-drawer
    side="right"
    show-if-above
    :width="200"
    :breakpoint="700"
    elevated
    class="bg-secondary text-white"
  >
    <q-scroll-area class="fit">
      <div class="q-pa-sm">
        <div v-for="node in previousNodes" :key="node.id">
          <a @click="$emit('gotoNode', node.id)" href="javascript:;">
            {{ node.id }}</a
          >
        </div>
      </div>
    </q-scroll-area>
  </q-drawer>
</template>

<script lang="ts">
import { Node } from 'src/models/node.model';
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'NodeHistorySideDrawer',

  props: {
    previousNodes: {
      type: Array<Node>,
      required: true,
    },
  },

  emits: ['gotoNode'],
});
</script>
