<template>
    <Icon :icon="props.icon" :class="props.className" />
  </template>
  <script setup lang="ts">
  import { Icon } from '@iconify/vue';
  const props = defineProps<{
    icon: string;
    className?: string;
  }>();
  </script>