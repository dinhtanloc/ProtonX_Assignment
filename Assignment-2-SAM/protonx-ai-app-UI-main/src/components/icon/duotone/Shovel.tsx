import React, { SVGProps } from 'react';

const SvgShovel = (props: SVGProps<SVGSVGElement>) => {
	return (
		<svg viewBox='0 0 24 24' className='svg-icon' {...props}>
			<g fill='none' fillRule='evenodd'>
				<path d='M0 0h24v24H0z' />
				<path
					d='M6.343 4.929L13.414 12 12 13.414l-7.071-7.07H1.893a.5.5 0 01-.353-.854l3.95-3.95a.5.5 0 01.853.353V4.93z'
					fill='currentColor'
					opacity={0.3}
				/>
				<path
					d='M16.95 9.879l2.825 3.26a5.517 5.517 0 011.24 4.695l-.399 1.998a1 1 0 01-.784.784l-1.998.4a5.517 5.517 0 01-4.696-1.241l-3.26-2.825 7.072-7.071zm-3.405 6.145c-.763-.646-1.732.499-.969 1.145l2.298 1.944c.764.646 1.733-.499.97-1.145l-2.299-1.944z'
					fill='currentColor'
				/>
			</g>
		</svg>
	);
};

export default SvgShovel;
