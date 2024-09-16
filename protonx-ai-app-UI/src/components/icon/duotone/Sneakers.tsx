import React, { SVGProps } from 'react';

const SvgSneakers = (props: SVGProps<SVGSVGElement>) => {
	return (
		<svg viewBox='0 0 24 24' className='svg-icon' {...props}>
			<g fill='none' fillRule='evenodd'>
				<path d='M0 0h24v24H0z' />
				<rect fill='currentColor' opacity={0.3} x={2} y={3} width={7} height={14} rx={1} />
				<path
					d='M16.624 13.054c2.203.804 3.559.742 4.376.946.584.146 1.105.453 1.561.92a2 2 0 01-.997 3.35c-1.29.286-2.82.483-4.592.59-2.98.182-8.11.186-15.386.015a.6.6 0 01-.586-.6v-6.202c4.25-.41 7.098-1.566 8.544-3.466a.6.6 0 01.917-.045c.415.447.806.853 1.173 1.22a1.01 1.01 0 00-.067.102l-1.5 2.598a1 1 0 001.732 1l1.335-2.311c.496.415.924.716 1.283.902.121.063.24.124.358.182l-.708 1.227a1 1 0 001.732 1l.825-1.428z'
					fill='currentColor'
				/>
			</g>
		</svg>
	);
};

export default SvgSneakers;
