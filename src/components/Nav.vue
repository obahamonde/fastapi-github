<script setup lang="ts">
import { useAuth0 } from '@auth0/auth0-vue'
const { loginWithPopup } = useAuth0()
const toggler = ref(false)
const nav = reactive({
    iconClass: toggler.value ? 'tl fixed x2 m-4 p-1 scale-125 text-secondary dark:text-light fade-in' : 'tl fixed x2 m-1 rounded  text-primary m-4 p-1 scale-125 z-50 dark:text-light fade-in-left',
    bar: toggler.value ? 'hidden' : 'h-screen  col w-17 tl fixed bg-success dark:bg-primary fade-in-left',
})
</script>
<template>
    <button @click="toggler= !toggler">
        <Ico :icon="toggler ? 'mdi-menu' : 'mdi-close'" :class-name="toggler ?'tl fixed x2 m-4 p-1 scale-125 text-secondary dark:text-light z-50 fade-in-down' : 'tl fixed x2 m-1 rounded  text-primary m-4 p-1 scale-125 z-50 dark:text-light fade-in-left'"      />
    </button>
    <section v-if="toggler">
    HELLO
    </section>
    <section v-else>
        <div :class="nav.bar">
            <button @click="loginWithPopup">
            <Ico icon="mdi-account" class="m-4  p-1 z-50 tl fixed mt-16 x2 scale-110 text-primary dark:text-light"
            
            /></button>
        <Router-Link to="/">
            <Ico icon="mdi-home" class="m-4 p-1 z-50 tl fixed mt-28 x2 scale-110 text-primary dark:text-light" />
        </Router-Link>
        </div>
    </section>
</template>
