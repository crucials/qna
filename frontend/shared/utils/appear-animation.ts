/**
 * @returns reactive flag variable that indicates whether
 * animation styles must be applied now
 */
export function useAppearAnimation() {
    const readyToAnimate = ref(false)
    
    onMounted(() => {
        // hack to make animation noticeable when navigating from other pages
        setTimeout(() => readyToAnimate.value = true, 1)
    })

    return { readyToAnimate }
}
