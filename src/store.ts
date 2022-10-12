import { defineStore, acceptHMRUpdate } from 'pinia'

export const useState = defineStore("state", () => {
    const state = reactive({})
    const setState = (payload: any) => {
        Object.assign(state, payload)
    }
    return {
        state,
        setState
    }
})

if (import.meta.hot) {
    import.meta.hot.accept(acceptHMRUpdate(useState, import.meta.hot))
}
