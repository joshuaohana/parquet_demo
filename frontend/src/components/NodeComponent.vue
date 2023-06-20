<template>
  <transition name="node-appear" mode="out-in">
    <div v-if="rootNode" class="node-root cursor-not-allowed" ref="rootNode">
      <div class="circle circle-big bg-dark">
        <span class="text-white text-subtitle1">{{ text }}</span>
      </div>
    </div>
    <div v-else class="cursor-pointer node-neighbor">
      <div class="circle bg-accent" @click.stop="$emit('click')">
        <span class="text-white text-subtitle1">{{ text }}</span>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: 'NodeComponent',
  props: {
    text: {
      type: String,
      required: true,
    },
    rootNode: {
      type: Boolean,
      default: false,
    },
  },
  emits: ['click'],
  watch: {
    text() {
      if (this.rootNode) {
        // refresh animation
        this.$nextTick(() => {
          const nodeElement = this.$refs.rootNode;
          nodeElement.classList.add('node-root');
          setTimeout(() => {
            nodeElement.classList.remove('node-root');
          }, 500);
        });
      }
    },
  },
};
</script>

<style scoped lang="scss">
.circle {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: auto 5px;

  &.circle-big {
    width: 120px;
    height: 120px;
  }
}

.node-root {
  animation: node-appear-upper 0.5s;
}

.node-neighbor {
  animation: node-appear-neighbor 0.5s;
}

@keyframes node-appear-upper {
  from {
    opacity: 0;
    transform: scale(0.5);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

@keyframes node-appear-neighbor {
  from {
    opacity: 0;
    transform: translateX(-100px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}
</style>
