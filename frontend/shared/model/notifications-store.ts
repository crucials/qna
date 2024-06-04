interface Notification {
    id: number
    type: 'success' | 'error'
    message: string
}

export const useNotificationsStore = defineStore('notifications', () => {
    const notifications = ref<Notification[]>([])
    
    let lastNotificationId = ref(0)
    function showNotification(notification: Omit<Notification, 'id'>, secondsToShow = 5) {
        const newNotificationId = lastNotificationId.value + 1
        lastNotificationId.value = newNotificationId

        notifications.value.push({ id: newNotificationId, ...notification })

        if(notifications.value.length === 4) {
            notifications.value.shift()
        }
        
        setTimeout(() => {
            notifications.value = notifications.value.filter(notification =>
                notification.id !== newNotificationId)
        }, secondsToShow * 1000)
    }

    return { notifications, showNotification }
})
