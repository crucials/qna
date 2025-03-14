<script setup lang="ts">
import authorizedOnlyMiddleware from '~/shared/model/authorized-only-middleware'
import { useCurrentAccountStore } from '~/shared/model/current-account-store'
import { logout } from '~/pages/dashboard/model/logout'

definePageMeta({
    path: '/dashboard',
    middleware: authorizedOnlyMiddleware,
})

useHead({
    title: 'qna dashboard',
})

const { account } = storeToRefs(useCurrentAccountStore())
</script>

<template>
    <div v-if="account">
        <header class="flex justify-between gap-5 mb-12">
            <div>
                <div class="flex items-center gap-x-3 mb-2">
                    <svg
                        class="w-7"
                        viewBox="0 0 98 98"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg"
                    >
                        <g clip-path="url(#clip0_88_123)">
                            <circle cx="49" cy="49" r="49" fill="#262626" />
                            <path
                                d="M49 25C43.2031 25 38.5 29.7031 38.5 35.5C38.5 41.2969 43.2031 46 49 46C54.7969 46 59.5 41.2969 59.5 35.5C59.5 29.7031 54.7969 25 49 25ZM43.75 49.5C35.0273 49.5 28 56.5273 28 65.25V67C28 70.8828 31.1172 74 35 74H63C66.8828 74 70 70.8828 70 67V65.25C70 56.5273 62.9727 49.5 54.25 49.5H43.75Z"
                                fill="#3a3a3a"
                            />
                        </g>
                        <defs>
                            <clipPath id="clip0_88_123">
                                <rect width="98" height="98" fill="white" />
                            </clipPath>
                        </defs>
                    </svg>

                    <span
                        class="text-neutral-500 text-base font-medium break-all xs:text-sm"
                        >{{ account.name }}</span
                    >
                </div>

                <h1 class="font-bold text-4xl sm:text-3xl">
                    What do you want to do?
                </h1>
            </div>

            <button
                @click="logout"
                class="transition-transform duration-300 hover:scale-110"
            >
                <svg
                    class="w-10 sm:w-8"
                    viewBox="0 0 42 42"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                >
                    <g clip-path="url(#clip0_88_134)">
                        <path
                            d="M41.6026 20.3595C41.6193 20.3392 41.6337 20.3179 41.6492 20.2971C41.6679 20.2722 41.6872 20.2478 41.7045 20.2219C41.7212 20.1971 41.7356 20.1712 41.7509 20.1456C41.7649 20.1222 41.7796 20.0993 41.7925 20.0751C41.8065 20.049 41.8183 20.0222 41.8309 19.9956C41.8427 19.9704 41.8553 19.9456 41.866 19.9199C41.8766 19.8941 41.8852 19.8677 41.8947 19.8415C41.9046 19.8138 41.9152 19.7865 41.9238 19.7582C41.9317 19.732 41.9376 19.7053 41.9442 19.6788C41.9515 19.65 41.9596 19.6216 41.9654 19.5922C41.9714 19.5614 41.9751 19.5304 41.9795 19.4995C41.9831 19.474 41.988 19.4488 41.9906 19.423C42.0019 19.3081 42.0019 19.1924 41.9906 19.0775C41.988 19.0517 41.9832 19.0266 41.9795 19.0011C41.9751 18.9701 41.9714 18.9391 41.9653 18.9084C41.9595 18.879 41.9514 18.8507 41.9441 18.8219C41.9375 18.7953 41.9317 18.7686 41.9237 18.7424C41.9152 18.7142 41.9046 18.6868 41.8947 18.6593C41.8852 18.633 41.8766 18.6066 41.866 18.5808C41.8553 18.555 41.8427 18.5303 41.8309 18.5052C41.8183 18.4785 41.8065 18.4517 41.7925 18.4256C41.7797 18.4015 41.7649 18.3786 41.751 18.3551C41.7357 18.3295 41.7213 18.3037 41.7046 18.2788C41.6873 18.2529 41.668 18.2286 41.6494 18.2037C41.6338 18.1829 41.6193 18.1615 41.6026 18.1412C41.5663 18.097 41.5281 18.0544 41.4876 18.014C41.4873 18.0136 41.4871 18.0133 41.4867 18.013L36.237 12.7632C35.5536 12.0798 34.4456 12.0798 33.7622 12.7632C33.0788 13.4466 33.0788 14.5546 33.7622 15.238L36.0247 17.5005H26.2499C25.2834 17.5005 24.5 18.2839 24.5 19.2504C24.5 20.2168 25.2834 21.0003 26.2499 21.0003H36.0246L33.7621 23.2628C33.0787 23.9461 33.0787 25.0542 33.7621 25.7376C34.4455 26.4209 35.5535 26.4209 36.2369 25.7376L41.4867 20.4878C41.487 20.4874 41.4872 20.4871 41.4876 20.4868C41.5281 20.4463 41.5663 20.4038 41.6026 20.3595Z"
                            fill="white"
                        />
                        <path
                            d="M29.7504 24.4996C28.784 24.4996 28.0005 25.283 28.0005 26.2495V34.9992H21.0008V7.00099V7.00033C21.0008 6.22754 20.4939 5.54622 19.7538 5.32417L13.6747 3.50044H28.0006V12.2501C28.0006 13.2166 28.784 14 29.7505 14C30.7169 14 31.5004 13.2166 31.5004 12.2501V1.75054C31.5004 0.784091 30.7169 0.000642856 29.7505 0.000642856H1.75159C1.75142 0.000642856 1.75126 0.000642856 1.75109 0.000642856C1.69933 0.000560828 1.64807 0.00302166 1.59721 0.00745117C0.794484 0.0679877 0.271228 0.596001 0.0810871 1.22639C0.068865 1.26559 0.0582014 1.30562 0.0486861 1.34615C0.0477018 1.35049 0.0468815 1.35492 0.0458972 1.35935C0.036464 1.40102 0.0285893 1.44335 0.0221091 1.48625C0.0212068 1.49232 0.0202224 1.49831 0.0193201 1.50438C0.0138243 1.54351 0.0094768 1.58312 0.00660582 1.62324C0.00152009 1.68787 -3.84363e-05 1.75268 0.00160212 1.81748V36.7498C0.00160212 37.5839 0.590398 38.3022 1.40838 38.4657L18.9076 41.9656C19.9905 42.1822 21.0007 41.3539 21.0007 40.2497V38.499H29.7504C30.7169 38.499 31.5003 37.7156 31.5003 36.7491V26.2496C31.5003 25.283 30.7169 24.4996 29.7504 24.4996ZM17.5009 38.1151L3.50149 35.3152V4.10319L17.5009 8.30301V36.7491V38.1151Z"
                            fill="white"
                        />
                    </g>
                    <defs>
                        <clipPath id="clip0_88_134">
                            <rect width="42" height="42" fill="white" />
                        </clipPath>
                    </defs>
                </svg>
            </button>
        </header>

        <ul
            class="grid grid-cols-[repeat(3,281px)] gap-5 m:grid-cols-[repeat(auto-fit,minmax(200px,1fr))]"
        >
            <li class="aspect-square m:aspect-auto rounded-lg">
                <NuxtLink
                    to="/dashboard/surveys/create"
                    class="block border border-transparent w-full h-full bg-black rounded-lg p-8 transition-colors duration-300 hover:border-white"
                >
                    <svg
                        class="w-12 mb-7"
                        viewBox="0 0 51 51"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg"
                    >
                        <rect
                            x="-1"
                            y="1"
                            width="49"
                            height="49"
                            rx="24.5"
                            transform="matrix(1 0 0 -1 2 51)"
                            stroke="white"
                            stroke-width="2"
                        />
                        <path
                            d="M13 25.5H38M25.5 13V38"
                            stroke="white"
                            stroke-width="4"
                            stroke-linecap="round"
                        />
                    </svg>

                    <span class="text-3xl"> Create new survey </span>
                </NuxtLink>
            </li>

            <li class="aspect-square m:aspect-auto rounded-lg">
                <NuxtLink
                    to="/dashboard/surveys"
                    class="block border border-transparent w-full h-full bg-black rounded-lg p-8 transition-colors duration-300 hover:border-white"
                >
                    <SurveyIcon class="mb-7" />

                    <span class="text-3xl"> Browse my surveys and data </span>
                </NuxtLink>
            </li>
        </ul>
    </div>
</template>
