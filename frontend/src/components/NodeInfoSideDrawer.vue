<template>
  <q-drawer
    side="left"
    show-if-above
    :width="200"
    :breakpoint="700"
    elevated
    class="bg-primary text-white"
  >
    <q-scroll-area class="fit">
      <div v-if="nodeStore.currentNode">
        <q-item v-for="(field, idx) in infoFields" :key="idx">
          <q-item-section>
            <q-item-label>{{ field.label }}</q-item-label>
          </q-item-section>
          <q-item-section>{{ field.getField() }}</q-item-section>
        </q-item>
      </div>
    </q-scroll-area>
  </q-drawer>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useNodeStore } from 'src/stores/node-store';

export default defineComponent({
  name: 'NodeInfoSideDrawer',

  setup() {
    const nodeStore = useNodeStore();
    return {
      nodeStore: nodeStore,
      infoFields: [
        {
          label: 'Node ID',
          getField: () => nodeStore.currentNode?.id,
        },
        {
          label: 'Neighbors',
          getField: () => nodeStore.currentNode?.neighbors?.length,
        },
        {
          label: 'Foo',
          getField: () => nodeStore.currentNode?.foo,
        },
        {
          label: 'Bar',
          getField: () => nodeStore.currentNode?.bar,
        },
        {
          label: 'Baz',
          getField: () => nodeStore.currentNode?.baz,
        },
        {
          label: 'Qux',
          getField: () => nodeStore.currentNode?.qux,
        },
        {
          label: 'Quux',
          getField: () => nodeStore.currentNode?.quux,
        },
        {
          label: 'Corge',
          getField: () => nodeStore.currentNode?.corge,
        },
      ],
    };
  },
});
</script>
